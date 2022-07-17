<template>
    <div class="polaroid">
      <img class="fit-img" :src="img"/>
      <h4 style="margin: 0; font-family: 'Brush Script MT', cursive; font-size: 32;  color: black;">
      {{ moment }}
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
    moment: {
      type: Object,
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
    width: 370px;
    height: 425px;
}

.polaroid {
    display: inline-block;
    overflow: hidden;
    background-color: white;
    width: 400px;
    height: 500px;
    margin: 10px 15px 45px;
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
