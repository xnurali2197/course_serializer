class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_name']

    def get_teacher_name(self, obj):
        return f"{obj.teacher.firstname} {obj.teacher.lastname}"
