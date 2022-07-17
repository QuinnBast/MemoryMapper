<template>
  <q-layout>
    <div class="bg-img">
      <img class="full-img" src="~/assets/images/WoodWall.jpg"/>
    </div>
    <create-moment-modal v-model="showCreateModal"></create-moment-modal>
    <q-page-container>
      <div id="map" class="flex flex-center half-map"></div>
      <div class="row" v-if="memory != null">
        <div class="col-8" style="text-align: center;">
          <h2>{{ memory.name }}</h2>
          <h3>{{ memory.description }}</h3>
        </div>
        <div class="col-4">
          <q-btn rounded color="secondary" icon="play_arrow" style="margin-top: 100px;">
            <p style="padding-top: 15px; font-size: 18px;">&nbsp;Play Memory</p>
          </q-btn>
        </div>
      </div>
      <CreateMemoryCard title="Add a moment" @click="openCreateModal"/>

      <polaroid-image-large
        v-for="moment in moments"
        :key="moment.FileId"
        :img="require('../assets/images/PenguinDate.jpg')"
        :moment="moment">
        {{ moment }}
      </polaroid-image-large>
      Moments: {{ moments }}

      <div>
        <q-btn rounded class="present-btn" color="secondary" icon="play_arrow">
          <p style="padding-top: 15px; font-size: 18px;">&nbsp;Play Memory</p>
        </q-btn>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue';
import L from 'leaflet';
import axios from 'axios';
import CreateMemoryCard from '../components/CreateMemoryCard.vue';
import PolaroidImageLarge from '../components/PolaroidImageLarge.vue';
import CreateMomentModal from '../components/CreateMomentModal.vue';

export default defineComponent({
  name: 'IndexPage',
  components: { CreateMemoryCard, PolaroidImageLarge, CreateMomentModal },
  data() {
    return {
      map: null,
      marker: null,
      showCreateModal: false,
      memory: null,
      moments: [{ t: 't' }, {}, {}, {}],
    };
  },
  methods: {
    goto() {
      const offsetLat = Math.random() * 20 - 10;
      const offsetLng = Math.random() * 20 - 10;
      const latlng = new L.LatLng(39.82 + offsetLat, -98.58 + offsetLng);
      L.popup()
        .setLatLng(latlng)
        .setContent('<img src="https://picsum.photos/600" width="120px" height="120px">')
        .openOn(this.map);
      this.map.flyTo(new L.LatLng(39.82, -98.58));
    },
    getMemory() {
      const self = this;
      axios.get(`http://localhost:8000/memory/${this.$route.params.id}`).then((response) => {
        self.memory = response.data;
      }).catch((error) => {
        console.info(error);
      });
    },
    getMoments() {
      const self = this;
      axios.get(`http://localhost:8000/memory/${this.$route.params.id}/moments`).then((response) => {
        self.moments = response.data;
        self.moments = [{ t: 't' }, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}];
      }).catch((error) => {
        console.info(error);
      });
    },
    openCreateModal() {
      this.showCreateModal = true;
    },
  },
  mounted() {
    this.getMemory();
    this.getMoments();
    this.map = L.map('map').setView([39.82, -98.58], 3);
    L.tileLayer(
      'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
      {
        attribution: 'Tiles &copy; Esri 2012',
        maxZoom: 19,
      },
    ).addTo(this.map);
  },
});
</script>

<style scoped>
#map {
  width: 300px;
  height: 300px;
  border: 1px solid black;
  position: fixed;
  bottom: 0;
  left: 0;
}

.half-map { width: 100%; height: 300px; }

.present-btn {
  position: fixed;
  bottom: 0;
  right: 0;
  margin: 20px;
}

.full-img {
    width: 100%;
    height: 100%;
}

.bg-img {
    margin-top: -50px;
    z-index: -5000;
    width: 100%;
    height: 100%;
    max-width: 100%;
    max-height: 100%;
    position: absolute;
    object-fit: cover;
}
</style>
