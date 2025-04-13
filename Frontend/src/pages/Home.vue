<script lang="ts" setup>
import RouterIcon from "../components/RouterIcon.vue";
</script>
<template>
  <h1 class="font-primary text-center font-bold text-3xl">Bienvenido/a 👋</h1>

  <div class="flex lg:flex-row flex-col gap-4 my-5 mx-2 text-center">
    <div
      class="rounded-md border-2 p-2 w-full lg:w-1/3 items-center flex flex-col gap-5 border-black"
    >
      <p class="font-primary text-2xl font-semibold">Acciones del Sistema</p>
      <div class="flex flex-col gap-2 w-full items-center">
        <RouterIcon icon="user" text="Padrón de Socios" />
        <RouterIcon icon="assembly" text="Asamblea de Socios" />
        <RouterIcon icon="tag" text="Deudas de Socios" />
      </div>
    </div>
    <div
      class="rounded-md border-2 p-2 w-full lg:w-2/3 items-center flex flex-col gap-5 border-black"
    >
      <p class="font-primary text-2xl font-semibold">Deudas Totales</p>
      <div class="flex flex-col gap-2 w-full items-center">
        <p>dasdasml</p>
      </div>
    </div>
  </div>
</template>
