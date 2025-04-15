<script lang="ts" setup>
import RouterIcon from "../components/RouterIcon.vue";
import BasicContainer from "../components/BasicContainer.vue";
import MayorContainer from "../components/MayorContainer.vue";
</script>
<template>
  <h1 class="font-primary text-center font-bold text-3xl">Bienvenido/a 👋</h1>

  <MayorContainer>
    <BasicContainer container-type="1third">
      <p class="font-primary text-2xl font-semibold">Acciones del Sistema</p>
      <div class="flex flex-col gap-2 w-full items-center">
        <RouterIcon to="census" icon="user" text="Padrón de Socios" />
        <RouterIcon to="assembly" icon="assembly" text="Asamblea de Socios" />
        <RouterIcon to="debt" icon="tag" text="Deudas de Socios" />
      </div>
    </BasicContainer>

    <BasicContainer container-type="2thirds">
      <p class="font-primary text-2xl font-semibold">Deudas Totales</p>
      <div class="flex flex-col gap-2 w-full items-center">
        <p>dasdasml</p>
      </div>
    </BasicContainer>
  </MayorContainer>

  <BasicContainer>
    <p class="font-primary text-2xl font-semibold">Notificaciones 🔔</p>
  </BasicContainer>
</template>
