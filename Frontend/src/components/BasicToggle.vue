<script lang="ts" setup>
defineProps({
  text: {
    type: String,
    default: "Button",
  },
  focused: {
    type: Boolean,
    default: false,
  },
  color: {
    type: String,
    default: "black",
  },
});
const emits = defineEmits(["click"]);
</script>
<template>
  <button
    @click="$emit('click')"
    class="text-black border text-sm w-1/2 cursor-pointer hover:shadow-lg border-black shadow duration-150 font-primary font-light py-2 px-4 rounded"
    :class="
      focused && color == 'red'
        ? 'bg-red-300'
        : focused && color == 'blue'
        ? 'bg-blue-300'
        : focused && color == 'green'
        ? 'bg-green-300'
        : ''
    "
  >
    {{ text }}
  </button>
</template>
