<script>
import router from "@/router";
import Button from "@/components/UI/Button.vue";

function onSubmit(event) {
    event.preventDefault()

    let answer_list = new Set();
    let true_answers = new Set();
    let formData = new FormData(event.target);
    const equalSet = (xs, ys) =>
        xs.size === ys.size && [...xs].every((x) => ys.has(x));

    formData.forEach((value, key) => answer_list.add(parseInt(key.split('-')[1])));

    if (answer_list.size !== 0) {
        for (const answer of this.question.answers) {
            if (answer.is_true) {
                true_answers.add(answer.id)
            }
        }

        if (equalSet(true_answers, answer_list)) {
            this.true_answer_counter += 1
        }

        event.target.reset()
        this.question_counter += 1
        if (this.question_counter >= this.questions_list.length) {
            console.log(12)
        } else {
            this.question = this.questions_list[this.question_counter]
        }
    } else {
        alert('Необходимо выбрать хотя бы один вариант ответа.')
    }
}

export default {
    components: {Button},
    data() {
        return {
            questions_list: [],
            question_counter: 0,
            question: {},
            true_answer_counter: 0,
            router: router
        };
    },
    methods: {
        onSubmit: onSubmit,
        calculatePercentage: (correct_answers, total_questions) => {
            if (total_questions === 0) {
                return 0;
            }

            const percentage = (correct_answers / total_questions) * 100;
            return Math.round(percentage);
        }
    },
    async mounted() {
        const token = localStorage.getItem('auth_token')

        if (token) {
            const quiz_id = document.URL.split('/').pop()
            let response = await fetch(`http://127.0.0.1:8000/api/v1/quiz/${quiz_id}`, {
                method: 'GET',
                headers: {
                    'Authorization': `Token ${token}`
                }
            });

            let response_data = await response.json()

            if (response_data.detail) {
                await router.push('/auth');
            } else {
                this.questions_list = response_data
                this.question = this.questions_list[this.question_counter]
            }
        } else {
            await router.push('/auth')
        }
    }
}
</script>

<template>
    <div class="container">
        <div class="question">
            <div v-if="this.question_counter < this.questions_list.length">
                <h2>{{ question.question }}</h2>
                <form @submit=onSubmit>
                    <div v-for="answer in question.answers">
                        <label class="custom-checkbox">
                            <input type="checkbox" :id="answer.id" :name="'answer-' + answer.id" :value="answer.id" class="custom-checkbox">
                            <span class="checkmark"></span>
                            {{ answer.text }}
                        </label>
                    </div>
                    <Button type="submit" text="Следующий" style="display: block; margin: 4vh auto 0;"></Button>
                </form>
            </div>
            <div v-else class="results">
                <h2>Результаты</h2>
                <p>Количество правильных ответов:
                    <strong>
                        {{ true_answer_counter }}/{{ questions_list.length }}
                    </strong>
                </p>
                <p>Вы решили верно тестирование на
                    <strong>
                        {{ calculatePercentage(true_answer_counter, questions_list.length) }}
                    </strong>%
                </p>
                <Button @click="router.push('/quiz')" text="Завершить" style="display: block; margin: 4vh auto 0;"></Button>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .container {
        padding: 20vh 0;
    }

    h2 {
        text-align: center;
        margin-bottom: 4vh;
        font-size: calc(var(--index) * 0.9);
    }

    .question {
        width: 30vw;
        padding: 4vh 4vw;
        border-radius: 20px;
        box-shadow: rgba(0, 0, 0, 0.7) 0px 5px 15px;
        background-color: rgba(255, 255, 255, 0.1);
    }

    form {
        display: flex;
        flex-direction: column;
    }

    p {
        margin-bottom: 2vh;
        text-align: center;
    }

    .custom-checkbox input {
        position: absolute;
        opacity: 0;
        cursor: pointer;
    }

    .custom-checkbox {
        display: inline-block;
        position: relative;
        padding-left: 2vw;
        margin-bottom: 2vh;
        cursor: pointer;
        font-size: calc(var(--index) * 0.9);
    }

    .custom-checkbox .checkmark {
        position: absolute;
        top: 0;
        left: 0;
        height: calc(var(--index) * 0.9);
        width: calc(var(--index) * 0.9);
        background-color: var(--color-header);
        border: 1px solid var(--color-header);
        border-radius: 3px;
    }

    .custom-checkbox input:checked + .checkmark {
        background-color: var(--color-blue-active);
        border: none;
    }

    .custom-checkbox input:checked + .checkmark:after {
        content: "";
        display: block;
        position: absolute;
        left: calc(var(--index) * 0.3);
        top: calc(var(--index) * 0.1);
        width: calc(var(--index) * 0.3);
        height: calc(var(--index) * 0.5);
        border: solid var(--color-header);
        border-width: 0 2px 2px 0;
        transform: rotate(45deg);
    }
</style>