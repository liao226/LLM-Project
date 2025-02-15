import {defineStore} from 'pinia';
import {loginApi as rootLogin, LoginData} from '/@/api/user';
import {UserState} from './types';
import {USER_ID, USER_NAME, USER_PASSWORD} from "/@/store/constants";

export const useUserStore = defineStore('user', {
    state: (): UserState => ({
        user_id: undefined,
        user_name: undefined,
        user_password: undefined,
    }),
    getters: {},
    actions: {

        // 管理员登录
        async adminLogin(loginForm: LoginData) {
            const result = await rootLogin(loginForm);
            console.log('result==>', result)

            if (result.code === 0) {
                this.$patch((state) => {
                    state.user_id = result.data.id
                    state.user_name = result.data.username
                    state.user_password = result.data.password
                    console.log('state==>', state)
                })

                localStorage.setItem(USER_PASSWORD, result.data.password)
                localStorage.setItem(USER_NAME, result.data.username)
                localStorage.setItem(USER_ID, result.data.id)
            }

            return result;
        },
        // 管理员登出
        async adminLogout() {
            // await userLogout();
            this.$patch((state) => {
                localStorage.removeItem(USER_ID)
                localStorage.removeItem(USER_NAME)
                localStorage.removeItem(USER_PASSWORD)

                state.user_id = undefined
                state.user_name = undefined
                state.user_password = undefined
            })
        },
    },
});
