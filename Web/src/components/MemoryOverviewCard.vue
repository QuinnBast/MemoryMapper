<template>
    <q-card class="card-title-top my-box cursor-pointer q-hoverable"
      bordered
      v-ripple
      @click="viewMoments">
      <q-card-section horizontal>
        <q-img :src="randomUrl()">
          <div class="text-subtitle2 absolute-top text-center">
          {{ title }}
        </div>
        </q-img>
        <q-card-section class="full-width">
          <q-img :src="randomUrl()"/>
        </q-card-section>
        <q-card-section class="full-width">
          <q-img :src="randomUrl()"/>
        </q-card-section>
        <q-card-section class="full-width">
          <q-img :src="randomUrl()"/>
        </q-card-section>
      </q-card-section>
    </q-card>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'MemoryOverviewCard',
  props: {
    title: {
      type: String,
      required: true,
    },
    pictureId: {
      type: Number,
      required: true,
    },
  },
  methods: {
    viewMoments() {
      console.info(`User wants to view moments for ${this.title}`);
    },
    randomUrl() {
      return `https://picsum.photos/600?random=${Math.random() * 200}`;
    },
  },
  setup() {

  },
});
</script>

<style lang="sass" scoped>
.card-title-top
  margin: 40px
.full-width
  width: 100%
</style>
