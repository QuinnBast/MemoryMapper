<template>
    <q-card class="card-title-top my-box cursor-pointer q-hoverable"
      bordered
      v-ripple
      @click="viewMoments">
      <q-card-section horizontal>
        <q-img :src="imageUrls[0]">
          <div class="text-subtitle2 absolute-top text-center">
          {{ title }}
        </div>
        </q-img>
        <q-card-section class="full-width">
          <q-img :src="imageUrls[1]"/>
        </q-card-section>
        <q-card-section class="full-width">
          <q-img :src="imageUrls[2]"/>
        </q-card-section>
        <q-card-section class="full-width">
          <q-img :src="imageUrls[3]"/>
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
  data() {
    return {
      imageUrls: [
        'https://picsum.photos/600?random=1',
        'https://picsum.photos/600?random=2',
        'https://picsum.photos/600?random=3',
        'https://picsum.photos/600?random=4',
      ],
    };
  },
  methods: {
    viewMoments() {
      console.info(`User wants to view moments for ${this.title}`);
    },
  },
  setup() {
  },
});
</script>

<style lang="sass" scoped>
.card-title-top
  margin: 40px
  box-shadow: 10px 10px 10px rgba(0, 0, 0, 1)
.full-width
  width: 100%
</style>
