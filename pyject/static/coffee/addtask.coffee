$ = jQuery.noConflict()

$ ->
	html =
		addTask: (t, list) ->
			list.append (@getTaskHtml t)
			Dajaxice.todos.save_todo()

		getTaskHtml: (t) ->
			checkbox = ($ '<input type="checkbox">')
			label = ($ '<label>')
				.append(checkbox)
				.append($ "<div>#{ t.task }</div>")
			listitem = ($ '<li>')
				.append(label)
			checkbox.click ->
				if checkbox.is ':checked'
					t.completed = true
					listitem.addClass 'task-completed'
				else
					t.completed = false
					listitem.removeClass 'task-completed'
			listitem

	window.addtask =
		addTask: (form) ->
			if form.task.value
				t = (
					task: form.task.value
					time: parseFloat(form.time.value.replace ',', '.') or 0
					completed: false
				)
				html.addTask t, ($ '.m-todo-list', ($ form).parent())
				form.task.value = ''
				form.time.value = ''
				($ form.task).focus()
			false