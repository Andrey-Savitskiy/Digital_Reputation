import { createWebHistory, createRouter } from "vue-router";
import Auth from "@/components/pages/Auth.vue";
import Registration from "@/components/pages/Registration.vue";
import Quiz from "@/components/pages/Quiz.vue";
import Question from "@/components/pages/Question.vue";

const routes = [
    {
        path: "/",
        name: "main",
        component: Auth,
    },
    {
        path: "/auth",
        name: "auth",
        component: Auth,
    },
    {
        path: "/registration",
        name: "registration",
        component: Registration,
    },
    {
        path: "/quiz",
        name: "quiz",
        component: Quiz,
    },
    {
        path: "/questions/:id",
        name: "questions",
        component: Question,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;