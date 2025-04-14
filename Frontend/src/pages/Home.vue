<script lang="ts" setup>
import RouterIcon from "../components/RouterIcon.vue";
import BasicContainer from "../components/BasicContainer.vue";
</script>
<template>
  <h1 class="font-primary text-center font-bold text-3xl">Bienvenido/a 👋</h1>

  <div class="flex lg:flex-row flex-col gap-4 my-5 text-center">
    <BasicContainer container-type="1third">
      <p class="font-primary text-2xl font-semibold">Acciones del Sistema</p>
      <div class="flex flex-col gap-2 w-full items-center">
        <RouterIcon to="census" icon="user" text="Padrón de Socios" />
        <RouterIcon to="census" icon="assembly" text="Asamblea de Socios" />
        <RouterIcon to="census" icon="tag" text="Deudas de Socios" />
      </div>
    </BasicContainer>

    <BasicContainer container-type="2thirds">
      <p class="font-primary text-2xl font-semibold">Deudas Totales</p>
      <div class="flex flex-col gap-2 w-full items-center">
        <p>dasdasml</p>
      </div>
    </BasicContainer>
  </div>
  <BasicContainer>
    <p class="font-primary text-2xl font-semibold">Notificaciones 🔔</p>
  </BasicContainer>
</template>
