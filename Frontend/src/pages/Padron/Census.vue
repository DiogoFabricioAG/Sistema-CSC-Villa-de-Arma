<script lang="ts" setup>
import { computed, onMounted, ref, watch } from "vue";
import BasicButton from "../../components/BasicButton.vue";
import BasicContainer from "../../components/BasicContainer.vue";
import BasicToggle from "../../components/BasicToggle.vue";
import User from "../../components/icons/User.vue";
import MayorContainer from "../../components/MayorContainer.vue";
import DialogComponent from "../../components/DialogComponent.vue";
import DialogContainer from "../../components/DialogContainer.vue";
import BasicCheckbox from "../../components/BasicCheckbox.vue";
import { useMyToastStore } from "../../stores/Toast";
import {
  postSocios,
  getSocios,
  loadSocios,
} from "../../services/sociosServices";
import type { SocioResponse } from "../../types/sociosTypes";

const optionSelected = ref(-1);

const isOpen = ref(false);
const isCheck = ref(false);
const dialogOptions = ref(0);
const handleChange = (value: number) => {
  optionSelected.value = value;
};
const socioData = ref({
  nombre: "",
  apellido: "",
  categoria: "",
  celular: "",
  correo_electronico: "",
});

const handleCreate = async () => {
  postSocios(socioData.value)
    .then((response) => {
      console.log(response);
      toastStore.showToast(500, "Socio creado correctamente", "check");
    })
    .catch((error) => {
      console.error(error);
      toastStore.showToast(500, "Error al crear el socio", "wrong");
    });
};

const handleLoadSocios = () => {
  loadSocios()
    .then((response) => {
      console.log(response);
      toastStore.showToast(500, "Datos cargados correctamente", "check");
      getSocios()
        .then((response) => {
          console.log(response);
          sociosResponse.value = response;
        })
        .catch((error) => {
          console.error("Error fetching socios:", error);
        });
    })
    .catch((error) => {
      console.error(error);
      toastStore.showToast(500, "Error al cargar los datos", "wrong");
    });
  handleOpen(0);
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

const sociosResponse = ref<SocioResponse[]>([]);
const filtros = ref({
  fecha_inicio: "",
  fecha_fin: "",
  categoria: "",
});

const filteredData = computed(() => {
  return sociosResponse.value.filter((socio) => {
    const fechaIngreso = new Date(socio.fecha_ingreso);
    const fechaInicio = new Date(filtros.value.fecha_inicio);
    const fechaFin = new Date(filtros.value.fecha_fin);

    return (
      (!filtros.value.fecha_inicio || fechaIngreso >= fechaInicio) &&
      (!filtros.value.fecha_fin || fechaIngreso <= fechaFin) &&
      (!filtros.value.categoria ||
        socio.categoria
          .toLowerCase()
          .includes(filtros.value.categoria.toLowerCase()))
    );
  });
});
const handleClean = () => {
  filtros.value.fecha_inicio = "";
  filtros.value.fecha_fin = "";
  filtros.value.categoria = "";
  isCheck.value = false;
  toastStore.showToast(500, "Se limpiaron los Filtros", "alert");
};

onMounted(() => {
  getSocios()
    .then((response) => {
      console.log(response);
      sociosResponse.value = response;
    })
    .catch((error) => {
      console.error("Error fetching socios:", error);
    });
});
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
        <BasicButton text="Limpiar Filtros" @click="handleClean" />
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
                <th class="border-black border p-2">Fecha de Ingreso</th>
                <th class="border-black border p-2">Correo Electronico</th>
              </tr>
            </thead>
            <tbody class="bg-white text-black">
              <tr
                v-for="(item, index) in filteredData"
                :key="index"
                class="hover:bg-red-100 duration-150 cursor-pointer"
              >
                <td class="border-black border p-2">{{ item.nombre }}</td>
                <td class="border-black border p-2">{{ item.apellido }}</td>
                <td class="border-black border p-2">{{ item.celular }}</td>
                <td class="border-black border p-2">{{ item.categoria }}</td>
                <td class="border-black border p-2">
                  {{ item.fecha_ingreso }}
                </td>
                <td class="border-black border p-2">
                  {{ item.correo_electronico }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <form
          @submit="handleCreate()"
          v-else-if="optionSelected == 1"
          class="font-primary font-light w-full flex flex-col h-full gap-4 justify-between text-lg"
        >
          <div class="space-y-3">
            <div class="flex gap-4">
              <input
                class="p-2 border w-1/2 border-black focus:scale-105 focus:outline-red-500 duration-150"
                type="text"
                placeholder="Nombre del Socio"
                v-model="socioData.nombre"
              />
              <input
                class="p-2 border w-1/2 border-black focus:scale-105 focus:outline-red-500 duration-150"
                type="text"
                placeholder="Apellido del Socio"
                v-model="socioData.apellido"
              />
            </div>
            <div class="flex gap-4">
              <input
                class="p-2 border w-1/2 border-black focus:scale-105 focus:outline-red-500 duration-150"
                type="text"
                placeholder="Categoria del Socio"
                v-model="socioData.categoria"
              />
              <input
                class="p-2 border w-1/2 border-black focus:scale-105 focus:outline-red-500 duration-150"
                type="text"
                placeholder="Numero del Socio"
                v-model="socioData.celular"
              />
            </div>
            <input
              class="p-2 border w-full border-black focus:scale-105 focus:outline-red-500 duration-150"
              type="text"
              placeholder="Dirección de Correo Electrónico"
              v-model="socioData.correo_electronico"
            />
          </div>

          <BasicButton text="Crear Socio" />
        </form>
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
              v-model="filtros.fecha_inicio"
            />
            <input
              type="date"
              class="w-1/2 border border-black rounded-sm p-1"
              placeholder="Fecha de Fin"
              v-model="filtros.fecha_fin"
            />
          </div>
          <input
            class="p-2 border w-full border-black focus:scale-105 focus:outline-red-500 duration-150"
            type="text"
            placeholder="Categoria del Socio"
            v-model="filtros.categoria"
          />
          <div
            class="flex gap-2 mt-2 font-primary font-light justify-center items-center"
          >
            <BasicCheckbox :is-open="isCheck" />
            <label for="active">Activo</label>
          </div>
        </div>
      </DialogContainer>
      <DialogContainer title="Cargar datos" v-if="dialogOptions === 1">
        <div class="text-sm font-primary font-light mt-2 space-y-3">
          <div>
            <p>¿Seguro de cargar los datos de la asamblea?</p>
            <p class="text-xs">
              Ultima vez cargado: <span class="font-bold">29/04/2025</span>
            </p>
          </div>

          <BasicButton text="Cargar Datos" @click="handleLoadSocios()" />
        </div>
      </DialogContainer>
    </DialogComponent>
  </MayorContainer>
</template>
