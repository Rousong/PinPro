<template>
  <div class="editor">
    <div class="editor-buttons">
      <span class="icon-container" v-if="inOwnedBoard" @click="removeFromBoard">
          <b-icon
            type="is-light"
            icon="minus-box"
            custom-size="mdi-24px">
         </b-icon>
      </span>
      <span class="icon-container" @click="addToBoard">
          <b-icon
            type="is-light"
            icon="plus-box"
            custom-size="mdi-24px">
         </b-icon>
      </span>
      <span class="icon-container" @click="deletePin" v-if="isOwner">
         <b-icon
           type="is-light"
           icon="delete"
           custom-size="mdi-24px">
         </b-icon>
      </span>
      <span class="icon-container" v-if="isOwner" @click="editPin">
       <b-icon
         type="is-light"
         icon="pencil"
         custom-size="mdi-24px">
       </b-icon>
      </span>
    </div>
  </div>
</template>

<script>
import API from '../api';
import modals from '../modals';

export default {
  name: 'Editor',
  props: {
    currentBoard: {
      type: Object,
      default() {
        return {};
      },
    },
    currentUsername: {
      default: null,
      type: String,
    },
    pin: {
      default() {
        return {};
      },
      type: Object,
    },
  },
  computed: {
    isOwner() {
      return this.pin.author === this.currentUsername;
    },
    inOwnedBoard() {
      return (
        Object.values(this.currentBoard).length !== 0
        && this.currentBoard.submitter.username === this.currentUsername
      );
    },
  },
  methods: {
    addToBoard() {
      modals.openAdd2Board(this, this.pin, this.currentUsername);
    },
    removeFromBoard() {
      this.$buefy.dialog.confirm({
        message: this.$i18n.t('editUI.msg_remove'),
        onConfirm: () => {
          API.Board.removeFromBoard(this.currentBoard.id, [this.pin.id]).then(
            () => {
              this.$buefy.toast.open(this.$i18n.t('editUI.msg_remove_ok'));
              this.$emit('pin-remove-from-board-succeed', this.pin.id);
            },
            () => {
              this.$buefy.toast.open(
                { type: 'is-danger', message: this.$i18n.t('editUI.msg_remove_fail') },
              );
            },
          );
        },
      });
    },
    editPin() {
      const props = {
        username: this.currentUsername,
        existedPin: this.pin,
        isEdit: true,
      };
      modals.openPinEdit(
        this,
        props,
      );
    },
    deletePin() {
      this.$buefy.dialog.confirm({
        message: this.$i18n.t('editUI.msg_del_pin'),
        onConfirm: () => {
          API.Pin.deleteById(this.pin.id).then(
            () => {
              this.$buefy.toast.open(this.$i18n.t('editUI.msg_ok_pin'));
              this.$emit('pin-delete-succeed', this.pin.id);
            },
            () => {
              this.$buefy.toast.open(
                { type: 'is-danger', message: this.$i18n.t('editUI.msg_fail_pin') },
              );
            },
          );
        },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@import './editor';
</style>
