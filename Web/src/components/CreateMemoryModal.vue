<template>
    <q-dialog v-model="visible" no-backdrop-dismiss>
      <q-card class="modal-card">
          <q-bar class="bg-secondary text-white q-pa-lg">
            <div>Create Memory</div>

            <q-space />

            <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>Close</q-tooltip>
            </q-btn>
        </q-bar>
        <q-card-section>
            <q-form>
                <div class="q-pa-md">
                <b>Give your memory a name!</b>
                <q-input
                    outlined
                    v-model="name"
                    label="Memory Name"
                    :rules="[val => !!val || 'Field is required']">
                    <template v-slot:prepend>
                        <q-icon name="theaters" />
                    </template>
                </q-input>
                </div>
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
            </q-form>
        </q-card-section>

        <q-separator />

        <q-card-actions align="right">
          <q-btn v-close-popup color="secondary" label="Create" @click="validateAndSubmit"/>
          <q-btn v-close-popup color="dark" label="Cancel" />
        </q-card-actions>
      </q-card>
    </q-dialog>
</template>

<script>
import { defineComponent } from 'vue';
import axios from 'axios';

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
