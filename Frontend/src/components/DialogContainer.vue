<template>
  <div
    @click.stop
    class="absolute top-[50%] left-[50%] border-2 border-black translate-x-[-50%] translate-y-[-50%] bg-white rounded-lg shadow-lg p-6 z-10"
  >
    <slot></slot>
  </div>
</template>
