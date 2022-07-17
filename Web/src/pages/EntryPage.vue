<template>
    <div class="full">
        <div class="bg-img">
            <img class="full-img" src="~/assets/images/WoodWall.jpg"/>
        </div>
        <div class="row">
            <div class="col-2">
              <PolaroidImage :img="require('../assets/images/PenguinDate.jpg')" text="Penguins"/>
              <PolaroidImage :img="require('../assets/images/Banff.jpg')" text="Banff"/>
            </div>
            <div class="col-2" style="margin-top: 100px">
              <PolaroidImage :img="require('../assets/images/BanffInkPots.jpg')" text="Inkpots"/>
              <PolaroidImage :img="require('../assets/images/Dragon.jpg')" text="Glow Saskatoon"/>
            </div>
            <div class="col-2">
              <PolaroidImage :img="require('../assets/images/Koi.jpg')" text="Koi"/>
              <PolaroidImage :img="require('../assets/images/KoiPond.jpg')" text="Boffins"/>
            </div>
            <div class="col-6 action">
                <q-btn color="secondary" @click="showMemories"><h2>Make memories</h2></q-btn>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import PolaroidImage from '../components/PolaroidImage.vue';

export default defineComponent({
  name: 'EntryPage',
  components: {
    PolaroidImage,
  },
  data() {
    return {
    };
  },
  methods: {
    showMemories() {
      this.$router.push('/memories/');
    },
  },
  setup() {

  },
});
</script>

<style scoped>
.full {
    height: 100vh;
    max-height: 100vh;
}

.full-img {
    width: 100%;
    height: 100%;
}

.fit-img {
    display: block;
    object-fit: cover;
    width: 220px;
    height: 255px;
}

.bg-img {
    z-index: -5000;
    width: 100%;
    height: 100%;
    max-width: 100%;
    max-height: 100%;
    position: absolute;
    object-fit: cover;
}

.action {
    display: -webkit-flexbox;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;
    -webkit-flex-align: center;
    -ms-flex-align: center;
    -webkit-align-items: center;
    align-items: center;
    justify-content: center;
    color: white;
    font-family: Garamond, serif;
    font-size: 32;
}
</style>
