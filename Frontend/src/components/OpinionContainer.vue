<script lang="ts" setup>
defineProps({
  title: {
    type: String,
    default: "Opiniones",
  },
  user: {
    type: String,
    default: "Usuario",
  },
  comment: {
    type: String,
    default: "Comentario",
  },
  date: {
    type: String,
    default: "Fecha",
  },
  rating: {
    type: Number,
    default: 0,
  },
});
</script>

<template>
  <div class="border-2 w-4/5 rounded-xl border-black p-4">
    <div class="flex justify-between w-full items-center mb-2">
      <h3 class="font-semibold text-xl">{{ title }}</h3>
      <span>{{ date }}</span>
    </div>
    <div class="flex items-center gap-2 mb-2">
      <p class="font-semibold">{{ user }}</p>
      <div class="flex items-center gap-1">
        <span v-for="i in rating" :key="i" class="text-yellow-500">⭐</span>
        <span v-for="i in 5 - rating" :key="i" class="text-gray-300">★</span>
      </div>
    </div>
    <p>{{ comment }}</p>
  </div>
</template>
