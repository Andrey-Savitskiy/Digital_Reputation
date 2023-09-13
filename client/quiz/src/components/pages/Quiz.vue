<script>
    import router from "@/router";

    export default {
        methods: {
            out: async () => {
                const token = localStorage.getItem('auth_token')
                let response = await fetch('http://127.0.0.1:8000/api/v1/auth/token/logout/', {
                    method: 'POST',
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                });
                localStorage.removeItem('auth_token')
                await router.push('/auth');
            }
        },
        data() {
            return {
                quiz_list: [],
                router: router
            };
        },
        async mounted() {
            const token = localStorage.getItem('auth_token')

            if (token) {
                let response = await fetch('http://127.0.0.1:8000/api/v1/quiz/', {
                    method: 'GET',
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                });

                let response_data = await response.json()

                if (response_data.detail) {
                    await router.push('/auth');
                } else {
                    this.quiz_list = response_data
                }
            } else {
                await router.push('/auth')
            }
        }
    }
</script>

<template>
    <div class="container">
        <p class="out" @click=out>Выйти</p>
        <h1>Список тестирований</h1>
        <ul v-if='quiz_list.length > 0'>
            <li @click="router.push(`/questions/${quiz.id}`)" v-for='quiz in quiz_list' :key='quiz.id' :id='quiz.id'>
                <h2>{{ quiz.title }}</h2>
                <p>{{ quiz.description }}</p>
            </li>
        </ul>
    </div>
</template>

<style scoped>
    .container {
        padding: 20vh 0;
    }

    h1 {
        text-align: center;
        margin-bottom: 5vh;
        font-size: calc(var(--index) * 1.5) !important;
    }

    h2 {
        font-size: calc(var(--index) * 0.9) !important;
    }

    p {
        font-size: calc(var(--index) * 0.7);
    }

    .out {
        display: flex;
        justify-content: end;
    }

    .out:hover {
        cursor: pointer;
    }

    li {
        list-style-type: none;
        width: 40vw;
        padding: 2vh 2vw;
        margin-bottom: 3vh;
        border-radius: 20px;
        box-shadow: rgba(0, 0, 0, 0.7) 0px 5px 15px;
        transition: var(--transition);
        background-color: rgba(255, 255, 255, 0.1);
    }

    li:hover {
        cursor: pointer;
        transform: scale(1.1);
    }
</style>