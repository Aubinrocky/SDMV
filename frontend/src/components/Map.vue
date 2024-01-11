<template>
    <div  class="h-screen w-screen">
      <l-map 
      ref="map" 
      :zoom="zoom" 
      :center="center">
        <l-tile-layer
          :url="urlStreetMap"
        ></l-tile-layer>
        <l-marker v-for="tournament in tournaments" 
            :key="tournament.id"
            :lat-lng="tournament.coords">
        </l-marker>
      </l-map>
    </div>
  </template>
  

<script>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker} from "@vue-leaflet/vue-leaflet";

export default {
  name: "Map",
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  props: {
    tournaments: {
      type: Array,
      required: true
    }
  },

  data() {
      return {
        zoom: 6,
        center: [47.044246576071195, 2.561126020147653],
        urlStreetMap: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      };
    },

};
</script>