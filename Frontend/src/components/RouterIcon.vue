<script lang="ts" setup>
import { defineProps } from "vue";
import User from "./icons/User.vue";
import Assembly from "./icons/Assembly.vue";
import Tag from "./icons/Tag.vue";
defineProps({
  icon: {
    type: String,
    required: true,
  },
  text: {
    type: String,
    required: true,
  },
});
</script>
<template>
  <router-link class="w-[60%]" to="">
    <div
      class="flex items-center duration-150 rounded-md border-2 border-black gap-2 p-4 cursor-pointer"
      :class="
        icon === 'user'
          ? 'hover:bg-red-100 '
          : icon === 'assembly'
          ? 'hover:bg-blue-100 '
          : 'hover:bg-green-100'
      "
    >
      <component
        :is="icon === 'user' ? User : icon === 'assembly' ? Assembly : Tag"
        class="w-10 h-10"
      />
      <span class="text-xs font-light font-primary">{{ text }}</span>
    </div>
  </router-link>
</template>
