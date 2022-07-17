<template>
    <div class="polaroid">
      <img class="fit-img" :src="img"/>
      <h4 style="margin: 0; font-family: 'Brush Script MT', cursive; font-size: 32; color: black;">
      {{ text }}
      </h4>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PolaroidImage',
  props: {
    img: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: true,
    },
  },
  setup() {

  },
});
</script>

<style scoped>
.fit-img {
    display: block;
    object-fit: cover;
    width: 240px;
    height: 290px;
}

.polaroid {
    overflow: hidden;
    background-color: white;
    width: 275px;
    height: 350px;
    margin: 55px 75px 45px;
    padding: 15px 15px 45px;
    text-align: center;
    text-decoration: none;
    -webkit-box-shadow: 0 4px 6px rgba(0, 0, 0, .3);
    -moz-box-shadow: 0 4px 6px rgba(0, 0, 0, .3);
    box-shadow: 0 4px 6px rgba(0, 0, 0, .3);
}

.polaroid:hover {
    -webkit-transform: scale(1.2);
    -moz-transform: scale(1.2);
    transform: scale(1.2);
    z-index: 10;
    -webkit-box-shadow: 0 10px 20px rgba(0, 0, 0, .7);
    -moz-box-shadow: 0 10px 20px rgba(0, 0, 0, .7);
    box-shadow: 0 10px 20px rgba(0, 0, 0, .7);
}
</style>
