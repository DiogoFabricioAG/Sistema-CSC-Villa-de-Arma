<script lang="ts" setup>
import { ref } from "vue";
import BasicButton from "../../components/BasicButton.vue";
import BasicContainer from "../../components/BasicContainer.vue";
import BasicToggle from "../../components/BasicToggle.vue";
import Assembly from "../../components/icons/Assembly.vue";
import MayorContainer from "../../components/MayorContainer.vue";
import ImageContainer from "../../components/ImageContainer.vue";
import DialogContainer from "../../components/DialogContainer.vue";
import DialogComponent from "../../components/DialogComponent.vue";
import { useMyToastStore } from "../../stores/Toast";

const optionSelected = ref(-1);

const handleChange = (value: number) => {
  optionSelected.value = value;
};
const toastStore = useMyToastStore();

const isOpen = ref(false);
const dialogOptions = ref(0);
const isCheck = ref(false);
const handleOpen = (value: number) => {
  isOpen.value = !isOpen.value;
  dialogOptions.value = value;
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
        <BasicButton text="Seleccionar Asamblea" @click="handleOpen(0)" />
        <BasicButton text="Cargar Asamblea" @click="handleOpen(1)" />
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
      <section class="w-full p-10 h-full relative">
        <div
          v-if="optionSelected == 0"
          class="mx-auto text-sm flex justify-center"
        >
          <ImageContainer id-image="1RrH6qE4jhPIPmIhN45yicV0ldB93rNom" />
        </div>
        <div
          v-if="optionSelected == 1"
          class="mx-auto text-sm flex justify-center"
        >
          <ImageContainer id-image="1RrH6qE4jhPIPmIhN45yicV0ldB93rNom" />
        </div>
      </section>
    </BasicContainer>

    <DialogComponent :is-open="isOpen" @close="handleOpen(0)">
      <DialogContainer title="Seleccionar Asamblea" v-if="dialogOptions === 0">
        <div class="text-sm font-primary mt-2 space-y-2">
          <p>Limite de Tiempo</p>
          <div class="flex justify-between gap-2 mx-auto">
            <input
              type="date"
              class="w-1/2 border border-black rounded-sm p-1"
              placeholder="Fecha de Inicio"
            />
            <input
              type="date"
              class="w-1/2 border border-black rounded-sm p-1"
              placeholder="Fecha de Fin"
            />
          </div>
          <table class="w-full border border-black">
            <thead class="bg-blue-200 border border-black">
              <tr>
                <th class="border border-black p-2">Fecha</th>
                <th class="border border-black p-2">Acción</th>
              </tr>
            </thead>
            <tbody>
              <tr class="border border-black">
                <td class="border border-black p-2">14/04/2025</td>
                <td class="border border-black p-2">
                  <button
                    class="bg-blue-100 border border-black p-1 rounded-sm cursor-pointer hover:bg-blue-200 duration-150"
                  >
                    Seleccionar
                  </button>
                </td>
              </tr>
              <tr class="border border-black">
                <td class="border border-black p-2">14/04/2025</td>
                <td class="border border-black p-2">
                  <button
                    class="bg-blue-100 border border-black p-1 rounded-sm cursor-pointer hover:bg-blue-200 duration-150"
                  >
                    Seleccionar
                  </button>
                </td>
              </tr>
              <tr class="border border-black">
                <td class="border border-black p-2">14/04/2025</td>
                <td class="border border-black p-2">
                  <button
                    class="bg-blue-100 border border-black p-1 rounded-sm cursor-pointer hover:bg-blue-200 duration-150"
                  >
                    Seleccionar
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </DialogContainer>
      <DialogContainer
        title="Cargar datos de Asamblea"
        v-if="dialogOptions === 1"
      >
        <div class="text-sm font-primary font-light mt-2 space-y-3">
          <div>
            <p>¿Seguro de cargar los datos de la asamblea?</p>
            <p class="text-xs">
              Ultima vez cargado: <span class="font-bold">29/04/2025</span>
            </p>
          </div>

          <BasicButton
            text="Cargar Datos"
            @click="
              () => {
                toastStore.showToast(500, 'Cargado Correctamente', 'check');
                isOpen = false;
              }
            "
          />
        </div>
      </DialogContainer>
    </DialogComponent>
  </MayorContainer>
</template>
