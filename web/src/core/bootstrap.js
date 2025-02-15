// localStorage恢复到内存

import {useUserStore} from "/@/store";
import {USER_ID, USER_NAME, USER_PASSWORD} from "/@/store/constants";

export default function Initializer() {
    const userStore = useUserStore()
    userStore.$patch((state) => {
        state.user_id = localStorage.getItem(USER_ID)
        state.user_name = localStorage.getItem(USER_NAME)
        state.user_password = localStorage.getItem(USER_PASSWORD)
        console.log('恢复store完毕==>', state)
    })

}
