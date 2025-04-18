<script lang="ts" setup>
defineProps({
  idImage: {
    type: String,
    required: true,
  },
});
</script>
<template>
  <iframe
    :src="`https://drive.google.com/file/d/${idImage}/preview`"
    width="500"
    height="360"
    allow="autoplay"
  ></iframe>
</template>
