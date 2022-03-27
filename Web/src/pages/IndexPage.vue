<template>
  <q-layout>
    <CreateMemoryModal v-model="showCreateModal"/>
    <q-page-container>
      <div class="row">
        <div class="col col-md-7 q-gutter-md q-pa-md">
          <q-scroll-area style="height: 100%;">
            <CreateMemoryCard title="Create a Memory" @click="activateCreateModal"/>
            <MemoryOverviewCard title="New York" pictureId=1 @mouseenter="goto"/>
            <MemoryOverviewCard title="San Fransisco" pictureId=5 @mouseenter="goto"/>
            <MemoryOverviewCard title="Bejing" pictureId=10 @mouseenter="goto"/>
            <MemoryOverviewCard title="Vancouver" pictureId=15 @mouseenter="goto"/>
            <MemoryOverviewCard title="Banff" pictureId=20 @mouseenter="goto"/>
            <MemoryOverviewCard title="Hawaii" pictureId=25 @mouseenter="goto"/>
            <MemoryOverviewCard title="Maui" pictureId=30 @mouseenter="goto"/>
            <MemoryOverviewCard title="Another Destination" pictureId=35 @mouseenter="goto"/>
            <MemoryOverviewCard title="Another" pictureId=40 @mouseenter="goto"/>
            <MemoryOverviewCard title="Some Long Name That I totally visited
            because I'm adventurous" @mouseenter="goto"/>
          </q-scroll-area>
        </div>
        <div class="col-6 col-md-5">
          <q-page id="map" class="flex flex-center"></q-page>
        </div>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue';
import L from 'leaflet';
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
    activateCreateModal() {
      this.showCreateModal = true;
    },
  },
  mounted() {
    this.map = L.map('map').setView([39.82, -98.58], 3);
    L.tileLayer(
      'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
      {
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',
        maxZoom: 19,
      },
    ).addTo(this.map);
  },
});
</script>

<style scoped>
#map { width: 100%; height: 100%; border: 1px solid black }
</style>
