import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {path: '/', name:"hosWelcome", component: () => import('../pages/HosWelcomePage.vue')},
    {path: '/home', component: () => import('../pages/HomeHos.vue')},
    {path: '/hosWelcome', component: () => import('../pages/HosWelcomePage.vue')},
    {path: '/userLogin', name:"userLogin", component: () => import('../pages/UserLoginPage.vue')},
    {path: '/userMenu', component: () => import('../pages/UserMenuPage.vue')},
    {path: '/userMenu/:number/:table/:order', name: 'userMenu', component: () => import('../pages/UserMenuPage.vue')},
    {path: '/userMenu/:number/:table/:order/userOrderSuccess', name: 'orderSuccess', component: () => import('../pages/UserOrderSuccessPage.vue')},
    {path: '/userMenu/:number/:table/:order/userPayment', component: () => import('../pages/UserPaymentPage.vue')},
    {path: '/userMenu/:number/:table/:order/userCardPay', component: () => import('../pages/UserCardPay.vue')},
    {path: '/userMenu/:number/:table/:order/userHelp', component: () => import('../pages/UserHelpPage.vue')},
    {path: '/userBye', component: () => import('../pages/UserByePage.vue')},
    {path: '/admin/:admin/containerMenu', component: () => import('../components/ContainerMenu.vue')},
    {path:'/admin/:admin/adminTable', component: () => import('../pages/AdminTablePage.vue')},
    {path:'/admin',name:"adminLogin", component: () => import('../pages/AdminLoginPage.vue')},
    {path:'/admin/:admin/adminMainMenu', name:"adminMainMenu", component: () => import('../pages/AdminMainMenu.vue')},


]
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router;