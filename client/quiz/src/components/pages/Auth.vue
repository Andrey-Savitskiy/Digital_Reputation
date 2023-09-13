<script setup>
import Button from "@/components/UI/Button.vue";
import router from "@/router";

async function onSubmit(event) {
    event.preventDefault()

    let object = {};
    let formData = new FormData(event.target);

    formData.forEach((value, key) => object[key] = value);

    let response = await fetch('http://127.0.0.1:8000/api/v1/auth/token/login/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(object),
    });

    let data = await response.json()

    if (data.auth_token) {
        localStorage.setItem('auth_token', data.auth_token)
        await router.push('/quiz');
    } else {
        alert('Введены некорректные данные')
    }
}
</script>

<template>
    <div class="container">
        <form @submit=onSubmit>
            <input type="text" name="username" id="username" placeholder="Логин">
            <input type="password" name="password" id="password" placeholder="Пароль">
            <Button type="submit" text="Войти" />
        </form>

        <router-link class="router-link" to="/registration">Регистрация</router-link>
    </div>
</template>

<style scoped>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    form {
        display: flex;
        flex-direction: column;
        margin-bottom: 1.5vh;
    }

    input {
        background-color: var(--color-header);
        border: 0;
        outline: none;
        padding: calc(var(--index) * 0.4) calc(var(--index) * 0.7);
        border-radius: 8px;
        font-weight: bold;
        font-size: calc(var(--index) * 0.7);
        margin-bottom: 1vh;
    }

    input:nth-last-child(2) {
        margin-bottom: 3vh;
    }

    .router-link {
        text-decoration: none;
        font-size: calc(var(--index) * 0.7);
    }

    .router-link:visited {
        color: var(--color-header);
    }
</style>