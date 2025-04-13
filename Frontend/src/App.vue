<script setup lang="ts">
import Header from "./components/Header.vue";
</script>

<template>
  <Header />
  <div class="w-[90vw] md:w-[80vw] my-2 mx-auto">
    <router-view />
  </div>
</template>
