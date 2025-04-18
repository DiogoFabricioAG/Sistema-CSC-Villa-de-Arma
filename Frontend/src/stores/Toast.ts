import { defineStore } from 'pinia'

export const useMyToastStore = defineStore(
    'myToastStore',
    {
        // Datos que iran en el store
        state: () => ({
            ms: 0,
            message: '',
            type: '',
            show: false,
        }),

        // Metodos y acciones que iran en el store
        actions: {
            showToast(ms: number, message: string, type: string) {
                this.ms = ms
                this.message = message
                this.type = type
                this.show = true
                setTimeout(() => {
                    this.show = false
                }, this.ms + 1000)
            },
        }
    }
)