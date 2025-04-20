<script lang="ts" setup>
import { ref } from "vue";
import BasicButton from "../../components/BasicButton.vue";
import BasicContainer from "../../components/BasicContainer.vue";
import BasicToggle from "../../components/BasicToggle.vue";
import Tag from "../../components/icons/Tag.vue";
import MayorContainer from "../../components/MayorContainer.vue";
import DialogComponent from "../../components/DialogComponent.vue";
import DialogContainer from "../../components/DialogContainer.vue";
import { useMyToastStore } from "../../stores/Toast";

const optionSelected = ref(-1);

const handleChange = (value: number) => {
  optionSelected.value = value;
};

const isOpen = ref(false);
const dialogOptions = ref(0);
const toastStore = useMyToastStore();

const handleOpen = (value: number) => {
  isOpen.value = !isOpen.value;
  dialogOptions.value = value;
};

// Mock data for members
const members = ref([
  { id: 1, name: "Juan Pérez", category: "Regular", debt: 250 },
  { id: 2, name: "María Gómez", category: "Premium", debt: 350 },
  { id: 3, name: "Carlos López", category: "Regular", debt: 150 },
]);

// Mock data for debts
const debts = ref([
  {
    id: 1,
    memberId: 1,
    concept: "Cuota mensual",
    amount: 150,
    date: "2023-05-01",
  },
  {
    id: 2,
    memberId: 1,
    concept: "Evento especial",
    amount: 100,
    date: "2023-05-15",
  },
  {
    id: 3,
    memberId: 2,
    concept: "Cuota mensual",
    amount: 350,
    date: "2023-05-01",
  },
]);

const selectedMember = ref<null | {
  id: number;
  name: string;
  category: string;
  debt: number;
}>(null);
const debtAmount = ref("");
const debtConcept = ref("");
const paymentAmount = ref("");
const paymentMethod = ref("");
const searchTerm = ref("");

const filteredMembers = ref([...members.value]);

const handleSearch = () => {
  if (!searchTerm.value) {
    filteredMembers.value = [...members.value];
    return;
  }

  filteredMembers.value = members.value.filter((member) =>
    member.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
};

const selectMember = (member) => {
  selectedMember.value = member;
  handleOpen(0); // Close the dialog
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
        <BasicButton text="Crear Deuda" @click="handleOpen(0)" />
        <BasicButton text="Saldar Deuda" @click="handleOpen(1)" />
        <BasicButton text="Seleccionar Socio" @click="handleOpen(2)" />
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
    <DialogComponent :is-open="isOpen" @close="handleOpen(0)">
      <DialogContainer title="Creación de Deuda" v-if="dialogOptions === 0">
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
            class="p-2 border w-full border-black focus:scale-105 focus:outline-green-500 duration-150"
            type="text"
            placeholder="Categoria del Socio"
          />

          <input
            v-model="debtAmount"
            class="p-2 border w-full border-black focus:scale-105 focus:outline-green-500 duration-150"
            type="number"
            placeholder="Monto de la Deuda"
          />
          <input
            v-model="debtConcept"
            class="p-2 border w-full border-black focus:scale-105 focus:outline-green-500 duration-150"
            type="text"
            placeholder="Concepto de la Deuda"
          />
          <select
            class="p-2 border w-full border-black focus:scale-105 focus:outline-green-500 duration-150"
          >
            <option value="" disabled selected>Tipo de Deuda</option>
            <option value="mensual">Cuota Mensual</option>
            <option value="evento">Evento Especial</option>
            <option value="multa">Multa</option>
          </select>

          <BasicButton
            text="Crear Deuda"
            @click="
              () => {
                toastStore.showToast(500, 'Deuda creada exitosamente', 'check');
                handleOpen(0);
              }
            "
          />
        </div>
      </DialogContainer>
      <DialogContainer title="Saldar Deuda" v-else-if="dialogOptions === 1">
        <div class="text-sm font-primary mt-2 space-y-2">
          <p class="font-semibold text-base">Deudas Pendientes</p>

          <div class="max-h-40 overflow-y-auto border border-black">
            <table class="font-primary font-light w-full">
              <thead class="bg-green-400 text-white sticky top-0">
                <tr class="border-black border">
                  <th class="border-black border p-2">Concepto</th>
                  <th class="border-black border p-2">Monto</th>
                  <th class="border-black border p-2">Fecha</th>
                </tr>
              </thead>
              <tbody class="bg-white text-black">
                <tr
                  v-for="debt in debts"
                  :key="debt.id"
                  class="hover:bg-green-100 duration-150 cursor-pointer"
                >
                  <td class="border-black border p-2">{{ debt.concept }}</td>
                  <td class="border-black border p-2">S/. {{ debt.amount }}</td>
                  <td class="border-black border p-2">{{ debt.date }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <input
            v-model="paymentAmount"
            class="p-2 border w-full border-black focus:scale-105 focus:outline-green-500 duration-150"
            type="number"
            placeholder="Monto a Pagar"
          />

          <input
            type="date"
            class="w-full border border-black rounded-sm p-2"
            placeholder="Fecha de Pago"
          />

          <select
            v-model="paymentMethod"
            class="p-2 border w-full border-black focus:scale-105 focus:outline-green-500 duration-150"
          >
            <option value="" disabled selected>Método de Pago</option>
            <option value="efectivo">Efectivo</option>
            <option value="transferencia">Transferencia Bancaria</option>
            <option value="tarjeta">Tarjeta de Crédito/Débito</option>
          </select>

          <BasicButton text="Registrar Pago" @click="handleOpen(0)" />
        </div>
      </DialogContainer>
      <DialogContainer
        title="Seleccionar Socio"
        v-else-if="dialogOptions === 2"
      >
        <div class="text-sm font-primary mt-2 space-y-3">
          <div class="flex gap-2">
            <input
              v-model="searchTerm"
              class="p-2 border w-full border-black focus:scale-105 focus:outline-green-500 duration-150"
              type="text"
              placeholder="Buscar por nombre"
            />
            <BasicButton text="Buscar" @click="handleSearch" />
          </div>

          <div class="max-h-40 overflow-y-auto border border-black">
            <table class="font-primary font-light w-full">
              <thead class="bg-green-400 text-white sticky top-0">
                <tr class="border-black border">
                  <th class="border-black border p-2">Nombre</th>
                  <th class="border-black border p-2">Categoría</th>
                  <th class="border-black border p-2">Deuda Total</th>
                </tr>
              </thead>
              <tbody class="bg-white text-black">
                <tr
                  v-for="member in filteredMembers"
                  :key="member.id"
                  @click="selectMember(member)"
                  class="hover:bg-green-100 duration-150 cursor-pointer"
                >
                  <td class="border-black border p-2">{{ member.name }}</td>
                  <td class="border-black border p-2">{{ member.category }}</td>
                  <td class="border-black border p-2">S/. {{ member.debt }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div
            v-if="selectedMember"
            class="border border-green-400 p-2 rounded"
          >
            <p class="font-semibold">
              Socio seleccionado: {{ selectedMember.name }}
            </p>
            <p>Deuda total: S/. {{ selectedMember.debt }}</p>
          </div>
        </div>
      </DialogContainer>
    </DialogComponent>
  </MayorContainer>
</template>
