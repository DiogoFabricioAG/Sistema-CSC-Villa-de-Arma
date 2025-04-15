<script lang="ts" setup>
import { ref } from "vue";
import BasicButton from "../../components/BasicButton.vue";
import BasicContainer from "../../components/BasicContainer.vue";
import BasicToggle from "../../components/BasicToggle.vue";
import Tag from "../../components/icons/Tag.vue";
import MayorContainer from "../../components/MayorContainer.vue";

const optionSelected = ref(-1);

const handleChange = (value: number) => {
  optionSelected.value = value;
};
</script>
<template>
  <MayorContainer>
    <BasicContainer container-type="1fourth">
      <Tag class="size-[20vw]" />
      <p class="font-primary text-xl font-light text-center">
        Deudas de Socios
      </p>
      <div class="flex flex-col justify-center gap-2">
        <BasicButton text="Crear Deuda" @click="console.log(1)" />
        <BasicButton text="Saldar Deuda" @click="console.log(1)" />
        <BasicButton text="Seleccionar Socio" @click="console.log(1)" />
      </div>
    </BasicContainer>
    <BasicContainer container-type="3fourth">
      <div class="flex justify-between w-2/3 gap-2 mt-2">
        <BasicToggle
          text="Grafica de Deuda"
          color="green"
          :focused="optionSelected === 0"
          @click="handleChange(0)"
        />
        <BasicToggle
          text="Tipo de Grafica"
          color="green"
          :focused="optionSelected === 1"
          @click="handleChange(1)"
        />
      </div>
    </BasicContainer>
  </MayorContainer>
</template>
