<template>
  <header class="bg-gray-800 mb-5 text-white justify-center flex p-4 shadow-md">
    <router-link :to="{ name: 'Home' }" class="flex items-center h-20">
      <img
        src="../assets/Logo CSC Villa de Arma.png"
        alt="LOGO"
        class="h-full object-contain"
      />
      <h1 class="text-3xl font-primary font-bold ml-4">
        Sistema CSC Villa de Arma
      </h1>
    </router-link>
  </header>
</template>
