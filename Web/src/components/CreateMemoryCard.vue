<template>
    <q-card class="card-title-top" bordered>
      <q-btn class="full" color="secondary">
          <q-icon name="spa" />&nbsp;&nbsp;Create a memory!
      </q-btn>
    </q-card>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CreateMemoryCard',
  props: {
    title: {
      type: String,
      required: true,
    },
  },
  setup() {

  },
});
</script>

<style lang="sass" scoped>
.card-title-top
  margin: 40px
  height: 80px
.full
  width: 100%
  height: 100%
</style>
