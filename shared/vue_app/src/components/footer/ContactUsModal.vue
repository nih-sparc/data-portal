<template>
     <el-dialog :show-close="false" :visible.sync="visible" @open="resetForm">
        <bf-dialog-header slot="title" title="Request a 3rd Reviewer"/>

        <dialog-body>
          <p
            class="mb-24"
          >This participant will be blinded, randomized, and set to “In Review”. We’ll also send an email to your reviewer.</p>

          <!-- <el-form
            ref="adjudicatorForm"
            :model="adjudicatorForm"
            :rules="adjudicatorFormRules"
            label-position="top"
            @submit.native.prevent="submitAdjudicatorForm"
          >
            <el-form-item prop="selectedAdjudicator">
              <template slot="label">
                Adjudicator
                <span class="label-helper">required</span>
              </template>
              <el-select
                v-model="adjudicatorForm.selectedAdjudicator"
                value-key="id"
                placeholder="Please choose one"
              >
                <el-option
                  v-for="item in adjudicatorOptions"
                  :key="item.id"
                  :label="item.fullName"
                  :value="item.fullName"
                />
              </el-select>
            </el-form-item>
          </el-form> -->
        </dialog-body>

        <div slot="footer" class="dialog-footer">
          <bf-button class="secondary">Cancel</bf-button>

          <bf-button
            class="primary"

          >Send</bf-button>
        </div>
      </el-dialog>

</template>

<script>
    export default {
        name: 'ContactUsModal',
        props: {
            visible: {
                type: Boolean,
                default: false
            },
        },
    }
</script>

<style lang="scss" scoped>

</style>