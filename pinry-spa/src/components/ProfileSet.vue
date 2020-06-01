<template>
<div>
      <div class='modal-card'>
        <header class='modal-card-head'>
          <p class='modal-card-title'>Edit Preferences</p>
          <button class='delete'></button>
        </header>
        <section class='modal-card-body'>
          <label class='label'>Name</label>
          <p class='control'>
            <input class='input' placeholder='Text input' type='text'>
          </p>
          <label class='label'>Username</label>
          <p class='control has-icon has-icon-right'>
            <input class='input' placeholder='Text input' type='text' value='pmillerk'>
          </p>
          <label class='label'>Email</label>
          <p class='control has-icon has-icon-right'>
            <input class='input' placeholder='Email input' type='text' value='hello@'>
            <i class='fa fa-warning'></i>
            <span class='help is-danger'>This email is invalid</span>
          </p>
          <div class='control'>
            <div class='control-label is-pulled-left'>
              <label class='label'>Date of Birth</label>
            </div>
            <span>
              <span class='select'>
                <select>
                  <option>Month</option>
                  <option>With options</option>
                </select>
              </span>
              <span class='select'>
                <select>
                  <option>Day</option>
                  <option>With options</option>
                </select>
              </span>
              <span class='select'>
                <select>
                  <option>Year</option>
                  <option>With options</option>
                </select>
              </span>
            </span>
          </div>
          <label class='label'>Description</label>
          <p class='control'>
            <textarea class='textarea' placeholder='Describe Yourself!'></textarea>
          </p>
          <div class='content'>
            <h1>Optional Information</h1>
          </div>
          <label class='label'>Phone Number</label>
          <p class='control has-icon has-icon-right'>
            <input class='input' placeholder='Text input' type='text' value='+1 *** *** 0535'>
          </p>
          <label class='label'>Work</label>
          <p class='control has-icon has-icon-right'>
            <input class='input' placeholder='Text input' type='text' value='Greater Washington Publishing'>
          </p>
          <label class='label'>School</label>
          <p class='control has-icon has-icon-right'>
            <input class='input' placeholder='Text input' type='text' value='George Mason University'>
          </p>
        </section>
        <footer class='modal-card-foot'>
          <a class='button is-warning modal-save'>Save changes</a>
          <a class='button modal-cancel'>Cancel</a>
        </footer>
      </div>
    </div>
</template>

<script>
export default {
  name: 'ProfileSet',
};
</script>

<style scoped>

</style>
