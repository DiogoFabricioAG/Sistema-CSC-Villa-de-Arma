<script lang="ts" setup>
defineProps({
  isOpen: {
    type: Boolean,
    default: false,
  },
});
const emits = defineEmits(["close"]);
</script>
<template>
  <div
    class="absolute top-0 right-0 h-[100vh] w-full bg-black/50"
    :class="isOpen ? '' : 'hidden'"
    @click="$emit('close')"
  >
    <slot></slot>
  </div>
</template>
