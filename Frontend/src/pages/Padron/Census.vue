<script lang="ts" setup>
import { ref } from "vue";
import BasicButton from "../../components/BasicButton.vue";
import BasicContainer from "../../components/BasicContainer.vue";
import BasicToggle from "../../components/BasicToggle.vue";
import User from "../../components/icons/User.vue";
import MayorContainer from "../../components/MayorContainer.vue";
import DialogComponent from "../../components/DialogComponent.vue";
import DialogContainer from "../../components/DialogContainer.vue";
import BasicCheckbox from "../../components/BasicCheckbox.vue";
import { useMyToastStore } from "../../stores/Toast";

const optionSelected = ref(-1);

const isOpen = ref(false);
const isCheck = ref(false);
const dialogOptions = ref(0);
const handleChange = (value: number) => {
  optionSelected.value = value;
};
const handleOpen = (dialogOption: number) => {
  isOpen.value = isOpen.value ? false : true;
  console.log(isOpen.value);
  if (dialogOption !== undefined) {
    dialogOptions.value = dialogOption;
  }
};
const myItemFile = ref<File | null>(null);
const toastStore = useMyToastStore();

const handleFileUpload = (event: Event) => {
  const fileInput = event.target as HTMLInputElement;
  const file = fileInput.files?.[0];
  if (file) {
    myItemFile.value = file;

    // Create a new Blob and trigger download
    const blob = new Blob([file], { type: file.type });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = `new_${file.name}`;
    link.click();
    URL.revokeObjectURL(link.href);
  }
};
</script>
<template>
  <MayorContainer>
    <BasicContainer container-type="1fourth">
      <User class="size-[20vw]" />
      <p class="font-primary text-xl font-light text-center">
        Padrón de Socios
      </p>
      <div class="flex flex-col justify-center gap-2">
        <BasicButton text="Filtrar Socios" @click="handleOpen(0)" />
        <BasicButton
          text="Limpiar Filtros"
          @click="
            toastStore.showToast(500, 'Se limpiaron los Archivos', 'alert')
          "
        />
        <BasicButton text="Actualizar Datos" @click="handleOpen(1)" />
      </div>
      <p>Cantidad de Socios: 1900</p>
    </BasicContainer>
    <BasicContainer container-type="3fourth">
      <div class="flex justify-between w-2/3 gap-2 mt-2">
        <BasicToggle
          text="Lista de Socios"
          color="red"
          :focused="optionSelected === 0"
          @click="handleChange(0)"
        />
        <BasicToggle
          text="Registrar Socio"
          color="red"
          :focused="optionSelected === 1"
          @click="handleChange(1)"
        />
      </div>
      <section class="w-full p-10 h-full relative">
        <div
          v-if="optionSelected == 0"
          class="mx-auto text-sm flex justify-center"
        >
          <table class="font-primary font-light">
            <thead class="bg-red-400 text-white">
              <tr class="border-black border">
                <th class="border-black border p-2">Nombre</th>
                <th class="border-black border p-2">Apellido</th>
                <th class="border-black border p-2">N° Celular</th>
                <th class="border-black border p-2">Categoría</th>
                <th class="border-black border p-2">Correo Electronico</th>
              </tr>
            </thead>
            <tbody class="bg-white text-black">
              <tr class="hover:bg-red-100 duration-150 cursor-pointer">
                <td class="border-black border p-2">Juan</td>
                <td class="border-black border p-2">Pérez</td>
                <td class="border-black border p-2">12345678</td>
                <td class="border-black border p-2">01/01/1990</td>
                <td class="border-black border p-2">diogo.abregu.g@uni.pe</td>
              </tr>
              <tr class="hover:bg-red-100 duration-150 cursor-pointer">
                <td class="border-black border p-2">María</td>
                <td class="border-black border p-2">Gómez</td>
                <td class="border-black border p-2">87654321</td>
                <td class="border-black border p-2">02/02/1985</td>
                <td class="border-black border p-2">diogo.abregu.g@uni.pe</td>
              </tr>
              <tr class="hover:bg-red-100 duration-150 cursor-pointer">
                <td class="border-black border p-2">Juan</td>
                <td class="border-black border p-2">Pérez</td>
                <td class="border-black border p-2">12345678</td>
                <td class="border-black border p-2">01/01/1990</td>
                <td class="border-black border p-2">diogo.abregu.g@uni.pe</td>
              </tr>
              <tr class="hover:bg-red-100 duration-150 cursor-pointer">
                <td class="border-black border p-2">María</td>
                <td class="border-black border p-2">Gómez</td>
                <td class="border-black border p-2">87654321</td>
                <td class="border-black border p-2">02/02/1985</td>
                <td class="border-black border p-2">diogo.abregu.g@uni.pe</td>
              </tr>
              <tr class="hover:bg-red-100 duration-150 cursor-pointer">
                <td class="border-black border p-2">Juan</td>
                <td class="border-black border p-2">Pérez</td>
                <td class="border-black border p-2">12345678</td>
                <td class="border-black border p-2">01/01/1990</td>
                <td class="border-black border p-2">diogo.abregu.g@uni.pe</td>
              </tr>
              <tr class="hover:bg-red-100 duration-150 cursor-pointer">
                <td class="border-black border p-2">María</td>
                <td class="border-black border p-2">Gómez</td>
                <td class="border-black border p-2">87654321</td>
                <td class="border-black border p-2">02/02/1985</td>
                <td class="border-black border p-2">diogo.abregu.g@uni.pe</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div
          v-else-if="optionSelected == 1"
          class="font-primary font-light w-full flex flex-col h-full gap-4 justify-between text-lg"
        >
          <div class="space-y-3">
            <div class="flex gap-4">
              <input
                class="p-2 border w-1/2 border-black focus:scale-105 focus:outline-red-500 duration-150"
                type="text"
                placeholder="Nombre del Socio"
              />
              <input
                class="p-2 border w-1/2 border-black focus:scale-105 focus:outline-red-500 duration-150"
                type="text"
                placeholder="Apellido del Socio"
              />
            </div>
            <div class="flex gap-4">
              <input
                class="p-2 border w-1/2 border-black focus:scale-105 focus:outline-red-500 duration-150"
                type="text"
                placeholder="Categoria del Socio"
              />
              <input
                class="p-2 border w-1/2 border-black focus:scale-105 focus:outline-red-500 duration-150"
                type="text"
                placeholder="Numero del Socio"
              />
            </div>
            <input
              class="p-2 border w-full border-black focus:scale-105 focus:outline-red-500 duration-150"
              type="text"
              placeholder="Dirección de Correo Electrónico"
            />
          </div>

          <BasicButton text="Crear Socio" @click="handleOpen(0)" />
        </div>
        <div
          class="absolute top-[40%] left-[27.5%] font-primary text-2xl font-lg"
          v-else
        >
          <p>Selecciona alguna opcion</p>
        </div>
      </section>
    </BasicContainer>
    <DialogComponent :is-open="isOpen" @close="handleOpen(0)">
      <DialogContainer title="Filtro de Socios" v-if="dialogOptions === 0">
        <div class="text-sm font-primary mt-2 space-y-2">
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
          <input
            class="p-2 border w-full border-black focus:scale-105 focus:outline-red-500 duration-150"
            type="text"
            placeholder="Categoria del Socio"
          />
          <div
            class="flex gap-2 mt-2 font-primary font-light justify-center items-center"
          >
            <BasicCheckbox :is-open="isCheck" />
            <label for="active">Activo</label>
          </div>
        </div>
      </DialogContainer>
      <DialogContainer title="Cargar Archivos" v-if="dialogOptions === 1">
        <div class="text-sm font-primary font-light mt-2 space-y-2">
          <label>
            <input type="file" hidden @change="handleFileUpload" />
            <div
              class="flex h-9 font-primary px-2 mb-2 hover:bg-gray-100 duration-150 flex-col border border-black text-black text-sm items-center justify-center cursor-pointer focus:outline-none"
            >
              Seleccionar Archivo
            </div>
          </label>
          <div>
            <p class="text-sm font-bold">No cuentas con el Formato?</p>
            <button
              class="flex h-9 w-full font-primary mt-2 px-2 flex-col border hover:bg-red-300 duration-150 bg-red-200 border-black text-black text-sm items-center justify-center cursor-pointer focus:outline-none"
            >
              Seleccionar Archivo
            </button>
          </div>
        </div>
      </DialogContainer>
    </DialogComponent>
  </MayorContainer>
</template>
