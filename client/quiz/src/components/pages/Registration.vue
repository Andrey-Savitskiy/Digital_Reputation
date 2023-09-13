<script setup>
import Button from "@/components/UI/Button.vue";
import router from "@/router";

async function onSubmit(event) {
    event.preventDefault()

    let password_field = document.getElementById('password').value
    let password_field_2 = document.getElementById('password_2').value

    if (password_field === password_field_2) {
        let object = {};
        let formData = new FormData(event.target);

        formData.forEach((value, key) => {
            if (key !== 'password_2') {
                object[key] = value
            }
        });

        let response = await fetch('http://127.0.0.1:8000/api/v1/auth/users/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(object),
        });

        let data = await response.json()

        if (data.id) {
            await router.push('/auth')
        } else if (data.username) {
            alert('Нельзя зарегистрировать пользователя с таким именем')
        } else if (data.password) {
            alert(data.password)
        }
    } else {
        alert('Пароли не совпадают')
    }
}
</script>

<template>
    <div class="container">
        <form @submit=onSubmit>
            <input type="text" name="username" id="username" placeholder="Логин">
            <input type="password" name="password" id="password" placeholder="Пароль">
            <input @change=onChange type="password" name="password_2" id="password_2" placeholder="Подтвердите пароль">
            <Button type="submit" text="Зарегистрироваться" />
        </form>

        <router-link class="router-link" to="/auth">Войти</router-link>
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