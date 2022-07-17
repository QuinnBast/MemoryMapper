<template>
    <q-dialog v-model="visible" no-backdrop-dismiss>
      <q-card class="modal-card">
          <q-bar class="bg-secondary text-white q-pa-lg">
            <div>Add a Moment</div>

            <q-space />

            <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>Close</q-tooltip>
            </q-btn>
        </q-bar>
        <q-card-section>
            <q-form>
                <div class="q-pa-md">
                <b>Provide some details</b>
                <q-input
                    type="textarea"
                    outlined
                    v-model="description" label="Description">
                    <template v-slot:prepend>
                        <q-icon name="description" />
                    </template>
                </q-input>
                </div>
                <div class="q-pa-md">
                <b>Upload a file</b>
                <div style="color: black">
                <q-file filled bottom-slots
                v-model="file" label="Upload Image" counter>
                  <template v-slot:prepend>
                    <q-icon name="cloud_upload" color="black" @click.stop.prevent />
                  </template>
                  <template v-slot:append>
                    <q-icon name="close" color="black" @click.stop.prevent="file = null"
                    class="cursor-pointer" />
                  </template>
                  <template v-slot:file>
                    <div style="color: black">{{ file.name }}</div>
                  </template>
                  <template v-slot:hint>
                    File to upload
                  </template>
                </q-file>
                </div>
                </div>
            </q-form>
        </q-card-section>

        <q-separator />

        <q-card-actions align="right">
          <q-btn v-close-popup color="secondary" label="Upload" @click="validateAndSubmit"/>
          <q-btn v-close-popup color="dark" label="Cancel" />
        </q-card-actions>
      </q-card>
    </q-dialog>
</template>

<script>
import { defineComponent, ref } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'CreateMomentModal',
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
      file: ref(null),
    };
  },
  methods: {
    validateAndSubmit() {
      const self = this;
      console.info('Validating');
      if (this.name !== '' && this.name != null) {
        const request = {
          memoryName: this.name,
          memoryDescription: this.description,
        };
        axios.put('http://localhost:8000/memory/', request).then((response) => {
          console.info(response);
          self.visible = false;
          console.info('Memory Created!');
          self.$emit('memoryCreated', response);
        }).catch((error) => {
          console.info(error);
          self.visible = true;
        });
      }
    },
    handleInput(value) {
      this.visible = value;
      this.$emit('input', value);
    },
  },
  setup() {

  },
});
</script>

<style lang="sass" scoped>
.modal-card
  min-width: 750px
  max-width: 70%
.wide
  min-width: 650px
</style>
