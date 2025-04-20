<script lang="ts" setup>
import RouterIcon from "../components/RouterIcon.vue";
import BasicContainer from "../components/BasicContainer.vue";
import MayorContainer from "../components/MayorContainer.vue";
import OpinionContainer from "../components/OpinionContainer.vue";
import { getOpinions } from "../services/opinionServices";
import { onMounted } from "vue";
import { ref } from "vue";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

import { Bar } from "vue-chartjs";

const data = {
  labels: [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ],
  datasets: [
    {
      label: "Data One",
      backgroundColor: "#f87979",
      data: [40, 20, 12, 39, 10, 40, 39, 20, 40, 20, 12, 11],
    },
  ],
};

const opinions = ref([]);
onMounted(() => {
  getOpinions()
    .then((response) => {
      opinions.value = response.data;
    })
    .catch((error) => {
      console.error("Error fetching opinions:", error);
    });
});
</script>
<template>
  <div>
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
          <Bar :data="data" :width="100" :height="35" />
        </div>
      </BasicContainer>
    </MayorContainer>

    <BasicContainer>
      <p class="font-primary text-2xl font-semibold">Notificaciones 🔔</p>
      <OpinionContainer
        v-for="(item, index) in opinions"
        :key="index"
        :title="item['Tema a Discutir']"
        :user="item['Nombre']"
        :comment="item['Descripción del Tema a Discutir']"
        :date="item['Marca temporal']"
        :rating="item['Calificación sobre el tema que quiere hablar']"
      />
    </BasicContainer>
  </div>
</template>
