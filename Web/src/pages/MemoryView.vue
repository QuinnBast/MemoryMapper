<template>
  <q-layout>
    {{ memory }}
    Viewing memory: {{ $route.params.id }}
    <q-page id="map" class="flex flex-center"></q-page>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue';
import L from 'leaflet';
import axios from 'axios';

export default defineComponent({
  name: 'IndexPage',
  components: { },
  data() {
    return {
      map: null,
      marker: null,
      showCreateModal: false,
      memory: null,
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
  },
  mounted() {
    this.getMemory();
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
