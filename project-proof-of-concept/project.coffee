$ = jQuery.noConflict()

html =
	tasks: $ '#tasks'
	tasklists: $ '#tasklists'

	addTaskList: (tl) ->
		@tasklists.append (@getTaskListHtml tl)

	addTask: (t, list) ->
		list.append (@getTaskHtml t)

	getTaskListHtml: (tl) ->
		listitem = ($ '<li>')
			.append("<h2>#{ tl.title }</h2>")
			.append(@tasks.html())
		listitem

	getTaskHtml: (t) ->
		checkbox = ($ '<input type="checkbox" class="checkbox">')
		listitem = ($ '<li>')
			.append(checkbox)
			.append("[#{ t.time }] ")
			.append(t.name)
		checkbox.click ->
			if checkbox.is ':checked'
				t.completed = true
				listitem.addClass 'completed'
			else
				t.completed = false
				listitem.removeClass 'completed'
		listitem

window.project =
	addTaskList: (form) ->
		if form.title.value
			tl = (
				title: form.title.value
			)
			html.addTaskList tl
			form.title.value = ''
		false

	addTask: (form) ->
		if form.message.value
			t = (
				name: form.message.value
				time: parseFloat(form.time.value.replace ',', '.') or 0
				assigned: parseInt(form.assigned.value)
				completed: false
			)
			html.addTask t, ($ '.tasks', ($ form).parent())
			form.message.value = ''
			form.time.value = ''
			form.assigned.value = ''
			($ form.message).focus()
		false

	showTaskForm: (button) ->
		($ button).hide()
		($ '.add-task-form', ($ button).parent()).show()