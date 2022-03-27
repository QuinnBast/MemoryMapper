<template>
    <q-dialog v-model="visible">
      <q-card class="my-card">
          <q-bar class="bg-secondary text-white q-pa-lg">
            <div>Create Memory</div>

            <q-space />

            <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>Close</q-tooltip>
            </q-btn>
        </q-bar>
        <q-card-section>
            <div class="q-pa-md">
                <q-input outlined v-model="name" label="Memory Name" />
            </div>
            <div class="q-pa-md">
                <q-input type="textarea" outlined v-model="description" label="Description" />
            </div>
            <div class="no-wrap items-center q-pa-md">
                <q-date v-model="dateRange" range />
            </div>
        </q-card-section>

        <q-separator />

        <q-card-actions align="right">
          <q-btn v-close-popup color="primary" label="Create" />
          <q-btn v-close-popup color="dark" label="Cancel" />
        </q-card-actions>
      </q-card>
    </q-dialog>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CreateMemoryModal',
  props: {
    value: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      visible: this.value,
      name: '',
      description: '',
      dateRange: null,
    };
  },
  methods: {
    handleInput(value) {
      this.visible = value;
      this.$emit('input', value);
    },
  },
  setup() {

  },
});
</script>
