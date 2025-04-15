<script lang="ts" setup>
import { ref } from "vue";
import BasicButton from "../../components/BasicButton.vue";
import BasicContainer from "../../components/BasicContainer.vue";
import BasicToggle from "../../components/BasicToggle.vue";
import Assembly from "../../components/icons/Assembly.vue";
import MayorContainer from "../../components/MayorContainer.vue";

const optionSelected = ref(-1);

const handleChange = (value: number) => {
  optionSelected.value = value;
};
</script>
<template>
  <MayorContainer>
    <BasicContainer container-type="1fourth">
      <Assembly class="size-[20vw]" />
      <p class="font-primary text-xl font-light text-center">
        Asambleas de Socios
      </p>
      <div class="flex flex-col justify-center gap-2">
        <BasicButton text="Seleccionar Asamblea" @click="console.log(1)" />
        <BasicButton text="Cargar Asamblea" @click="console.log(1)" />
      </div>
      <p>Fecha de Asamblea: 14/04/2025</p>
    </BasicContainer>
    <BasicContainer container-type="3fourth">
      <div class="flex justify-between w-2/3 gap-2 mt-2">
        <BasicToggle
          text="Lista de Asistentes"
          color="blue"
          :focused="optionSelected === 0"
          @click="handleChange(0)"
        />
        <BasicToggle
          text="Acta de Reunion"
          color="blue"
          :focused="optionSelected === 1"
          @click="handleChange(1)"
        />
      </div>
    </BasicContainer>
  </MayorContainer>
</template>
