<template>
  <el-dialog class="contact-modal" :show-close="true" :visible.sync="visible" @close="onClose">
    <div class="dialog-body">
      <div class="header">
        <h2>Subscribe to Mailing List</h2>
      </div>
      <el-form ref="form" :label-position="labelPosition" label-width="100px" :model="form" :rules="formRules">
        <el-form-item prop="name" label="Your Name">
          <el-input placeholder="Enter your name" v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item prop="email" label="Your Email">
          <el-input placeholder="Enter your email" type="email" v-model="form.email"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button class="send-button" @click="submitForm">Subscribe</el-button>
        </el-form-item>
      </el-form>
    </div>
  </el-dialog>
</template>

<script>
export default {
  name: 'ListservModal',
  data() {
    return {
      labelPosition: 'top',
      form: {
        name: '',
        email: ''
      },
      formRules: {
        name: [
          {
            required: true,
            message: 'Please enter your name',
            trigger: 'change'

          }
        ],

        email: [
          {
            required: true,
            message: 'Please enter your email',
            trigger: 'change'
          }
        ]
      },
    }
  },
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  },

  methods: {
    submitForm: function() {
      this.$refs.form.validate(valid => {
        if (!valid) {
          return;
        }
        this.sendRequest();
      });
    },

    sendRequest: function() {
      // send request logic goes here
      this.$http.post("/api/listserv-subscribe", {
        name: this.form.name,
        email: this.form.email
      })
      this.onClose()
    },

    onClose: function(){
      this.$emit('update:visible', false)
      this.$refs.form.resetFields();
    },

  }
};
</script>

<style lang="scss">
@import '../../styles/_contact-modal.scss';
</style>
