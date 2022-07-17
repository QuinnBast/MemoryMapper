<template>
  <q-layout>
    <div class="bg-img">
      <img class="full-img" src="~/assets/images/WoodWall.jpg"/>
    </div>
    <CreateMemoryModal v-model="showCreateModal" @memoryCreated="loadMemories"/>
    <q-page-container>
      <div class="row">
        <div class="col col-md-7 q-gutter-md q-pa-md">
          <CreateMemoryCard title="Create a Memory" @click="activateCreateModal"/>
          <q-scroll-area style="height: 75%;">
            <div v-if="memories.length > 0">
              <MemoryOverviewCard
              v-for="memory in memories"
              :key="memory.id"
              :title="memory.name"
              pictureId=1
              @mouseenter="goto"
              @click="viewMemory(memory.id)"/>
            </div>
            <div v-else>
              <h2 style="color: white">No memories! Create one to get started!</h2>
            </div>
          </q-scroll-area>
        </div>
        <div class="col-6 col-md-5">
          <div class="padded-map">
            <div id="map" class="flex flex-center"></div>
          </div>
        </div>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue';
import L from 'leaflet';
import axios from 'axios';
import MemoryOverviewCard from '../components/MemoryOverviewCard.vue';
import CreateMemoryCard from '../components/CreateMemoryCard.vue';
import CreateMemoryModal from '../components/CreateMemoryModal.vue';

export default defineComponent({
  name: 'IndexPage',
  components: {
    MemoryOverviewCard,
    CreateMemoryCard,
    CreateMemoryModal,
  },
  data() {
    return {
      map: null,
      marker: null,
      showCreateModal: false,
      memories: [],
    };
  },
  methods: {
    viewMemory(id) {
      this.$router.push(`/memory/${id}`);
    },
    goto() {
      const offsetLat = Math.random() * 20 - 10;
      const offsetLng = Math.random() * 20 - 10;
      const latlng = new L.LatLng(39.82 + offsetLat, -98.58 + offsetLng);
      L.popup()
        .setLatLng(latlng)
        .setContent('<img src="https://picsum.photos/600" width="120px" height="120px">')
        .openOn(this.map);
      this.map.flyTo(new L.LatLng(latlng.lat, latlng.lng), 11);
    },
    loadMemories() {
      const self = this;
      axios.get('http://localhost:8000/memory/').then((response) => {
        self.memories = response.data.items;
      }).catch((error) => {
        console.info(error);
      });
    },
    activateCreateModal() {
      this.showCreateModal = true;
    },
  },
  mounted() {
    this.loadMemories();
    this.map = L.map('map').setView([39.82, -98.58], 3);
    L.tileLayer(
      'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
      {
        attribution: '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        maxZoom: 19,
      },
    ).addTo(this.map);

    // L.tileLayer(
    // 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
    // {
    // maxZoom: 19,
    // },
    // ).addTo(this.map);
  },
});
</script>

<style scoped>
#map { width: 100%; height: 100%; border: 1px solid black }

.full-img {
    width: 100%;
    height: 100%;
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

.padded-map {
  overflow: hidden;
  height: 80vh;
  margin-top: 50px;
  margin-bottom: 150px;
  box-shadow: 30px 30px 30px rgba(0, 0, 0, 1);
}
</style>
