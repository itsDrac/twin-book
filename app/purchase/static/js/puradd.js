/**
 * Adjust the indices of form fields when removing items.
 */
  function adjustIndices(removedIndex) {
      var $forms = $('.subform');

      $forms.each(function(i) {
          var $form = $(this);
          var index = parseInt($form.data('index'));
          var newIndex = index - 1;

          if (index < removedIndex) {
              // Skip
              return true;
          }

          // Change ID in form itself
          $form.attr('id', $form.attr('id').replace(index, newIndex));
          $form.data('index', newIndex);

          // Change IDs in form inputs
          $form.find('input').each(function(j) {
              var $item = $(this);
              $item.attr('id', $item.attr('id').replace(index, newIndex));
              $item.attr('name', $item.attr('name').replace(index, newIndex));
          });
      });
  }

  /**
   * Remove a subform.
   */
  function removeForm() {
      var $removedForm = $(this).closest('.subform');
      var removedIndex = parseInt($removedForm.data('index'));

      $removedForm.remove();

      // Update indices
      adjustIndices(removedIndex);
  }

  /**
   * Add a new subform.
   */
  function addForm() {

      // Get Last index
      var $lastForm = $('.subform').last();

      var newIndex = 0;

      if ($lastForm.length > 0) {
          newIndex = parseInt($lastForm.data('index')) + 1;
      }

      // Add elements
      var $newForm = $lastForm.clone();

      $newForm.attr('id', 'item_quantity-'+ newIndex);
      $newForm.data('index', newIndex);

      ['select','input'].forEach( (field) => {
        let $item = $newForm.find(field)
        let old_id = $item.attr('id').replace( /(^.+\D)(\d+)(\D.+$)/i,'$2');
        $item.attr('id', $item.attr('id').replace(old_id, newIndex));
        $item.attr('name', $item.attr('name').replace(old_id, newIndex));
        
      });

      // Append
      $('#item-container').append($newForm);
      $newForm.addClass('subform');
      $newForm.removeClass('is-hidden');

      $newForm.find('.remove').click(removeForm);
  }


  $(document).ready(function() {
      $('#add').click(addForm);
      $('.remove').click(removeForm);
  });

