// 路由表
const constantRouterMap = [
    {
        path: '/',
        redirect: '/admin',
    },
    {
        path: '/adminLogin',
        name: 'adminLogin',
        component: () => import('/@/views/admin-login.vue'),
    },
    {
        path: '/admin',
        name: 'admin',
        redirect: '/admin/unitTest',
        component: () => import('/@/views/main.vue'),
        children: [
            {path: 'unitTest', name: 'unitTest', component: () => import('/@/views/unitTest.vue')},
            {path: 'integratedTest', name: 'integratedTest', component: () => import('/@/views/integratedTest.vue')},
            {path: 'questionBank', name: 'questionBank', component: () => import('/@/views/questionBank.vue')},
            {path: 'personalCenter', name: 'personalCenter', component: () => import('/@/views/personalCenter.vue')},
        ]
    },
];

export default constantRouterMap;
