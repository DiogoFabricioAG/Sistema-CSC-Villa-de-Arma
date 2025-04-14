<script lang="ts" setup>
import BasicButton from "../../components/BasicButton.vue";
import BasicContainer from "../../components/BasicContainer.vue";
import User from "../../components/icons/User.vue";
</script>
<template>
  <BasicContainer container-type="1fourth">
    <User class="size-[20vw]" />
    <p class="font-primary text-xl font-light text-center">Padrón de Socios</p>
    <div class="flex flex-col justify-center gap-2">
      <BasicButton text="Filtrar Socios" @click="console.log(1)" />
      <BasicButton text="Limpiar Filtros" @click="console.log(1)" />
      <BasicButton text="Actualizar Datos" @click="console.log(1)" />
    </div>
    <p>Cantidad de Socios: 1900</p>
  </BasicContainer>
</template>
