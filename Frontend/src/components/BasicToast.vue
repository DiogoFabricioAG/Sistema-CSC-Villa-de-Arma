<script lang="ts" setup>
import { useMyToastStore } from "../stores/Toast";
import Alert from "./icons/Alert.vue";
import Check from "./icons/Check.vue";
import Error from "./icons/Error.vue";

const store = useMyToastStore();
</script>

<template>
  <div
    class="transition ease-in-out select-none duration-500 border border-black bg-white font-primary font-light text-sm p-4 rounded-lg shadow-lg fixed bottom-7 right-5 z-50"
    :class="store.show ? 'opacity-100' : 'opacity-0'"
  >
    <div class="flex items-center gap-2">
      <Check v-if="store.type === 'check'" class="text-green-500" />
      <Alert v-else-if="store.type === 'alert'" class="text-orange-500" />
      <Error v-else-if="store.type === 'wrong'" class="text-red-500" />
      <p class="text-gray-800">{{ store.message }}</p>
    </div>
  </div>
</template>
