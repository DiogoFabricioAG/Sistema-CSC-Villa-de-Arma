<script setup lang="ts">
defineProps({
  containerType: {
    type: String,
    default: "full",
  },
});
</script>
<template>
  <div
    class="rounded-md border-2 p-2 items-center shadow-md flex flex-col gap-5 border-black"
    :class="
      containerType === 'full'
        ? 'w-full'
        : containerType === '2thirds'
        ? 'lg:w-2/3 w-full'
        : containerType === '1third'
        ? 'lg:w-1/3 w-full'
        : containerType === '1half'
        ? 'lg:w-1/2 w-full'
        : containerType === '1fourth'
        ? 'lg:w-1/4 w-full'
        : ''
    "
  >
    <slot></slot>
  </div>
</template>
