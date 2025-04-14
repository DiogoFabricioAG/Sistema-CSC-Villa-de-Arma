<script lang="ts" setup>
defineProps({
  text: {
    type: String,
    default: "Button",
  },
});
const emits = defineEmits(["click"]);
</script>
<template>
  <button
    @click="$emit('click')"
    class="text-black border text-sm cursor-pointer border-black shadow hover:bg-gray-100 duration-150 font-primary font-light py-2 px-4 rounded"
  >
    {{ text }}
  </button>
</template>
