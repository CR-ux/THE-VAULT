extends Area2D

signal hit

@export var speed = 400 #pixels/sec
var screen_size


func _ready():
	screen_size = get_viewport_rect().size
#	hide()

#The delta parameter in the _process() function refers to the frame length - 
# the amount of time that the previous frame took to complete. 
# Using this value ensures that your movement will remain consistent even if the frame rate changes.
func _process(delta):
	var velocity = Vector2.ZERO
	if Input.is_action_pressed("move_right"):
		velocity.x += 1
	if Input.is_action_pressed("move_left"):
		velocity.x -= 1
	if Input.is_action_pressed("move_down"):
		velocity.y += 1
	if Input.is_action_pressed("move_up"):
		velocity.y -= 1
	if velocity.length() > 0:
		velocity = velocity.normalized() * speed
		$AnimatedSprite2D.play()
	else:
		$AnimatedSprite2D.stop()
		
	position += velocity * delta
	position = position.clamp(Vector2.ZERO, screen_size)
	
	if velocity.x != 0:
		$AnimatedSprite2D.animation = "walk"
		$AnimatedSprite2D.flip_v = false
		$AnimatedSprite2D.flip_h = velocity.y < 0
	elif velocity.y != 0:
		$AnimatedSprite2D.animation = "stand"
		$AnimatedSprite2D.flip_h = velocity.x > 0
		


func _on_body_entered(_body: Node2D) -> void:
	hit.emit()
	$CollisionShape2D.set_deferred("disabled", true)
	
	
func start(pos):
	position = pos
	show()
	$CollisionShape2D.disabled = false
	
	
	
		
